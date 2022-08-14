using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using project.APP.Commands;
using project.App.Extensions;
using project.APP.Services;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.BL.Facade;
using project.BL.Models;
namespace project.APP.ViewModels
{
    public class MainPageViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly UserFacade _userFacade;
        private readonly CarFacade _carFacade;
        private readonly DriveFacade _driveFacade;
        public MainPageViewModel(IMediator mediator, UserFacade userFacade, CarFacade carFacade, DriveFacade driveFacade)
        {

            _mediator = mediator;
            _userFacade = userFacade;
            _carFacade = carFacade;
            _driveFacade = driveFacade;

            _mediator.Register<ShowMainPageMessage>(ShowMainPage);

            _mediator.Register<ShowCreateNewRideMessege>(HideMainPage);
            _mediator.Register<ShowLookForRideMessege>(HideMainPage);
            _mediator.Register<ShowMyCarMessege>(HideMainPage);
            _mediator.Register<ShowMyProfileMessege>(HideMainPage);
            _mediator.Register<ShowSettingsMessege>(HideMainPage);
            _mediator.Register<LogOutMessage>(HideMainPage);

            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);
            _mediator.Register<RidesUpdated>(UpdateRideList);
            _mediator.Register<SelectedRideDetailMessage<DetailDriveModel>>(UpdateSelectedRide);

            RideSelectedCommand = new RelayCommand<ListDriveModel>(RideSelected);
            UnreserveCommand = new AsyncRelayCommand(UnreserveAsync);

        }

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;
        private void ShowMainPage(ShowMainPageMessage obj)
        {
            PageVisibility = Visibility.Visible;
        }


        public async Task UnreserveAsync()
        {
            if (CurrentDriveModel == null || User == null)
            {
                throw new InvalidOperationException("Null model cannot be added");
            }

            await _driveFacade.RemovePassengerFromDrive(CurrentDriveModel.Id, User.Id);
            _mediator.Send(new RidesUpdated());
            CurrentDriveModel = DetailDriveModel.Empty;
        }


        private void RideSelected(ListDriveModel? ride) => _mediator.Send(new SelectedRideDetailMessage<DetailDriveModel> { Id = ride?.Id });

        public ICommand RideSelectedCommand { get; }

        public ICommand UnreserveCommand { get; }


        public DetailDriveModel? CurrentDriveModel { get; set; } = DetailDriveModel.Empty;

        private async void UpdateSelectedRide(SelectedRideDetailMessage<DetailDriveModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadRideAsync(id);
        }

        public async Task LoadRideAsync(Guid id)
        {
            CurrentDriveModel = await _driveFacade.GetAsync(id) ?? DetailDriveModel.Empty;
        }

        public ObservableCollection<ListDriveModel> Rides { get; set; } = new();


        private async void UpdateRideList(RidesUpdated obj) => await LoadRidesAsync();

        public async Task LoadRidesAsync()
        {
            Rides.Clear();
            var rides = _driveFacade.GetAllDrivesWhereUserIsPassenger(User.Id);
            Rides.AddRange(rides);
        }

        private void HideMainPage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;

        }

        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadAsync(id);
            _mediator.Send(new RidesUpdated());
            CurrentDriveModel = DetailDriveModel.Empty;
        }

        public DetailUserModel? User { get; set; } = DetailUserModel.Empty;

        public async Task LoadAsync(Guid id)
        {
            User = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
        }
    }
}

