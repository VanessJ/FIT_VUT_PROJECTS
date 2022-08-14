using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using System.Windows.Navigation;
using AutoMapper.Configuration;
using project.APP.Commands;
using project.App.Extensions;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;
using project.BL.Facade;
using project.BL.Models;

namespace project.APP.ViewModels
{
    public class LookForRideViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly DriveFacade _driveFacade;
        private readonly UserFacade _userFacade;
        public LookForRideViewModel(IMediator mediator, DriveFacade driveFacade, UserFacade userFacade)
        {
            _driveFacade = driveFacade;
            _userFacade = userFacade;
            //prijme singleton mediatoru a priradi ho do lokalni promenne at s nim muzem tady pracovat
            _mediator = mediator;
            
            //registruje k prijmu zpravy "ShowMainPageMessage" a pokud ji to prijme, zavola se metoda ShowMainPage
            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(HidePage);
            _mediator.Register<ShowLookForRideMessege>(ShowPage);
            _mediator.Register<ShowMyCarMessege>(HidePage);
            _mediator.Register<ShowMyProfileMessege>(HidePage);
            _mediator.Register<ShowSettingsMessege>(HidePage);
            _mediator.Register<LogOutMessage>(HidePage);
            _mediator.Register<RidesUpdated>(UpdateRideList);

            _mediator.Register<SelectedMessage<DetailDriveModel>>(UpdateSelectedRide);
            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);

            RideSelectedCommand = new RelayCommand<ListDriveModel>(RideSelected);
            ReserveCommand = new AsyncRelayCommand(ReserveAsync, CanReserve);
            FilterCommand = new AsyncRelayCommand(FilterAsync);

        }
        private void RideSelected(ListDriveModel? ride) => _mediator.Send(new SelectedMessage<DetailDriveModel> { Id = ride?.Id });
        public ICommand ReserveCommand { get; }
        public ICommand RideSelectedCommand { get; }
        public ICommand FilterCommand { get; }

        public Visibility SelectedVisibility { get; set; } = Visibility.Hidden;



    public DetailDriveModel? Model { get; set; } = DetailDriveModel.Empty;
        public DetailDriveModel? CurrentDriveModel { get; set; } = DetailDriveModel.Empty;

        public DetailDriveModel? FilterDriveModel { get; set; } = DetailDriveModel.Empty;

        public string StartDateFilter { get; set; } = string.Empty;
        public string DestinationFilter { get; set; } = string.Empty;
        public string FromFilter { get; set; } = string.Empty;

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;
        public ObservableCollection<ListDriveModel> Rides { get; set; } = new();
        public string SelectedRide { get; set; } = "None currently";
        public DetailUserModel? User { get; set; } = DetailUserModel.Empty;

        public bool NotInConflict { get; set; } = false;

        private void ShowPage(ShowLookForRideMessege obj)
        {
            PageVisibility = Visibility.Visible;

        }
        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;
            _mediator.Send(new RidesUpdated());

        }
        private async void UpdateRideList(RidesUpdated obj) => await LoadAsync();
        private async void UpdateSelectedRide(SelectedMessage<DetailDriveModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadRideAsync(id);

            SelectedRide = CurrentDriveModel?.JourneyBeginning ?? string.Empty;
            SelectedVisibility = Visibility.Visible;
            NotInConflict = !(await _driveFacade.IsUserInDrive(User.Id, CurrentDriveModel.Id));
        }
        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadUserAsync(id);
        }

        public async Task FilterAsync()
        {
            DateTime dateTime = DateTime.MinValue;
            string? from = null;
            string? destination = null;
            if (StartDateFilter != string.Empty)
            {
                dateTime = DateTime.ParseExact(StartDateFilter, "M/d/yyyy h:mm", null);
            }

            if (FromFilter != string.Empty)
            {
                from = FromFilter;
            }

            if (DestinationFilter != string.Empty)
            {
                destination = DestinationFilter;
            }

            var rides = await _driveFacade.Filter(dateTime, false, from, destination, User.Id);
            Rides.Clear();
            Rides.AddRange(rides);

        }

        public async Task ReserveAsync()
        {
            if (CurrentDriveModel == null || User == null)
            {
                throw new InvalidOperationException("Null model cannot be added");
            }

            await _driveFacade.AddPassengerToDrive(CurrentDriveModel.Id, User.Id);
            _mediator.Send(new RidesUpdated());
        }

        private bool CanReserve()
        {
            return NotInConflict;
        }

        private bool IsRideFull()
        {
            return !CurrentDriveModel.IsFull;
        }
        public async Task LoadRideAsync(Guid id)
        {
            CurrentDriveModel = await _driveFacade.GetAsync(id) ?? DetailDriveModel.Empty;
        }
        public async Task LoadUserAsync(Guid id)
        {
            User = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
        }
        public async Task LoadAsync()
        {
            Rides.Clear();
            var rides = await _driveFacade.GetAllDrivesUserIsNotIn(User.Id);
            Rides.AddRange(rides);
            CurrentDriveModel = DetailDriveModel.Empty;
            SelectedVisibility = Visibility.Hidden;
            NotInConflict = false;
        }
    }
}
