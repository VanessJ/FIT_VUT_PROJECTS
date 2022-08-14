using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Input;
using Microsoft.Toolkit.Mvvm.Input;
using project.App.Extensions;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;
using project.BL.Facade;
using project.BL.Models;
using AsyncRelayCommand = project.APP.Commands.AsyncRelayCommand;


namespace project.APP.ViewModels
{
    public class CreateNewRideViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly UserFacade _userFacade;
        private readonly CarFacade _carFacade;
        private readonly DriveFacade _driveFacade;
        public CreateNewRideViewModel(IMediator mediator, UserFacade userFacade, CarFacade carFacade, DriveFacade driveFacade)
        {
            
            _mediator = mediator;
            _userFacade = userFacade;
            _carFacade = carFacade;
            _driveFacade = driveFacade;


            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(ShowPage);
            _mediator.Register<ShowLookForRideMessege>(HidePage);
            _mediator.Register<ShowMyCarMessege>(HidePage);
            _mediator.Register<ShowMyProfileMessege>(HidePage);
            _mediator.Register<ShowSettingsMessege>(HidePage);
            _mediator.Register<LogOutMessage>(HidePage);

            _mediator.Register<CarsUpdated>(UpdateCarList);
            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);
            _mediator.Register<SelectedMessage<DetailCarModel>>(UpdateSelectedCar);
            _mediator.Register<SelectedRideDetailMessage<DetailDriveModel>>(UpdateSelectedRide);
            _mediator.Register<RidesUpdated>(UpdateRideList);
            _mediator.Register<SelectPassengerMessage<DetailUserModel>>(UpdateSelectedPassenger);


            DeletePassengerCommand = new AsyncRelayCommand(DeletePassenger, CanDeletePassenger);
            CarSelectedCommand = new Commands.RelayCommand<ListCarModel>(CarSelected);
            DriveSelectedCommand = new Commands.RelayCommand<ListDriveModel>(RideSelected);
            PassengerSelectedCommand =  new RelayCommand<ListUserModel>(PassegerSelected);
            SaveCommand = new AsyncRelayCommand(SaveAsync, CanSave);
            DeleteCommand = new AsyncRelayCommand(DeleteAsync, CanDelete);

        }

        public ICommand DeletePassengerCommand { get; }
        public ICommand PassengerSelectedCommand { get; }

        public ICommand SaveCommand { get; }

        public ICommand CarSelectedCommand { get; }

        public ICommand DriveSelectedCommand { get; }

        public ICommand DeleteCommand { get; }

        public DetailDriveModel? NewDriveModel { get; set; } = DetailDriveModel.Empty;
        public DetailDriveModel? SelectedDriveModel { get; set; } = DetailDriveModel.Empty;

        public DetailUserModel? Passenger { get; set; } = DetailUserModel.Empty;

        public DetailCarModel? SelectedCarModel { get; set; } = DetailCarModel.Empty;
        public DetailUserModel? User { get; set; } = DetailUserModel.Empty;

        public string StartDate { get; set; } = string.Empty;

        public string EndDate { get; set; } = string.Empty;

        public int? NumberOfSeats { get; set; } = null;


        public Visibility PageVisibility { get; set; } = Visibility.Hidden;

        private void CarSelected(ListCarModel? car) => _mediator.Send(new SelectedMessage<DetailCarModel> { Id = car?.Id });

        private void RideSelected(ListDriveModel? drive) => _mediator.Send(new SelectedRideDetailMessage<DetailDriveModel> { Id = drive?.Id });

        private void PassegerSelected(ListUserModel? drive) => _mediator.Send(new SelectPassengerMessage<DetailUserModel> { Id = drive?.Id });
        private void ShowPage(ShowCreateNewRideMessege obj)
        {
            PageVisibility = Visibility.Visible;

        }

        private bool CanSave() => IsRideValid();

        private bool IsRideValid()
        {
            return ((NewDriveModel?.JourneyBeginning != string.Empty) && (NewDriveModel?.JourneyBeginning != string.Empty) 
                                                                      && (StartDate != string.Empty) && (EndDate != string.Empty)
                                                                      && (SelectedCarModel != DetailCarModel.Empty)
                ) ;
        }

        private async void UpdateRideList(RidesUpdated obj) => await LoadRidesAsync();

        private async void UpdateCarList(CarsUpdated obj) => await LoadAsync();

        public async Task LoadRidesAsync()
        {
            Rides.Clear();
            var rides = _driveFacade.GetDrivesWithDriver(User.Id);
            Rides.AddRange(rides);


        }

        public async Task LoadAsync()
        {
            Cars.Clear();
            var cars = _carFacade.GetCarsOfDriver(User.Id);
            Cars.AddRange(cars);
            _mediator.Send(new RidesUpdated());
        }


        private async void UpdateSelectedPassenger(SelectPassengerMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            Passenger = await _userFacade.GetAsync(id);


        }

        private async Task DeletePassenger()
        {
            if (Passenger == DetailUserModel.Empty) return;
            await _driveFacade.RemovePassengerFromDrive(NewDriveModel.Id, Passenger.Id);
            NewDriveModel = await _driveFacade.GetAsync(NewDriveModel.Id);
            Passenger = DetailUserModel.Empty;
            UpdatePassengers();
            _mediator.Send(new SelectedRideDetailMessage<DetailDriveModel> { Id = NewDriveModel?.Id });
            


        }

        private async void UpdateSelectedRide(SelectedRideDetailMessage<DetailDriveModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadRideAsync(id);
            await LoadCarAsync(NewDriveModel.Car.Id);
            StartDate = NewDriveModel.DepartureTime.ToString(format: "M/d/yyyy h:mm");
            EndDate = NewDriveModel.ArrivalTime.ToString(format: "M/d/yyyy h:mm");

            UpdatePassengers();
            NumberOfSeats = await _driveFacade.NumberOfAvaliableSeats(NewDriveModel.Id);
            

        }

        private void UpdatePassengers()
        {
            Passengers.Clear();
            var passengers = _userFacade.GetPassengers(NewDriveModel.Id);
            Passengers.AddRange(passengers);

        }

        private async void UpdateSelectedCar(SelectedMessage<DetailCarModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadCarAsync(id);
        }

        public async Task LoadRideAsync(Guid id)
        {
            NewDriveModel = await _driveFacade.GetAsync(id) ?? DetailDriveModel.Empty;
        }

        public async Task LoadCarAsync(Guid id)
        {
            SelectedCarModel = await _carFacade.GetAsync(id) ?? DetailCarModel.Empty;
        }

        public async Task SaveAsync()
        {
            if (NewDriveModel == null)
            {
                throw new InvalidOperationException("Null model cannot be saved");
            }

            NewDriveModel.DriverId = User.Id;
            NewDriveModel.CarId = SelectedCarModel.Id;
            NewDriveModel.DepartureTime = DateTime.ParseExact(StartDate, "M/d/yyyy h:mm", null);
            NewDriveModel.ArrivalTime = DateTime.ParseExact(EndDate, "M/d/yyyy h:mm",null);
            NewDriveModel = await _driveFacade.SaveAsync(NewDriveModel);

            _mediator.Send(new RidesUpdated());
        }


        public async Task DeleteAsync()
        {
            if (NewDriveModel is null)
            {
                throw new InvalidOperationException("Null model cannot be deleted");
            }

            await _driveFacade.DeleteAsync(NewDriveModel);
            _mediator.Send(new RidesUpdated());
            NewDriveModel = DetailDriveModel.Empty;
            StartDate = string.Empty;
            EndDate = string.Empty;
            SelectedCarModel = DetailCarModel.Empty;
            NumberOfSeats = null;
        }


        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadAsync(id);
            _mediator.Send(new CarsUpdated());
        }

        public async Task LoadAsync(Guid id)
        {
            User = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
            NewDriveModel = DetailDriveModel.Empty;
            StartDate = string.Empty;
            EndDate = string.Empty;
            Passenger = DetailUserModel.Empty;
        }

        public ObservableCollection<ListCarModel> Cars { get; set; } = new();
        public ObservableCollection<ListDriveModel> Rides { get; set; } = new();

        public ObservableCollection<ListUserModel> Passengers { get; set; } = new();

        private bool CanDelete() => IsDeleteValid();

        private bool CanDeletePassenger()
        {
            return Passenger?.Id != Guid.Empty;
        }

        private bool IsDeleteValid()
        {
            return NewDriveModel?.Id != Guid.Empty;

        }



        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;
            SelectedCarModel = DetailCarModel.Empty;
            NewDriveModel = DetailDriveModel.Empty;
            StartDate = string.Empty;
            EndDate = string.Empty;
            Passenger = DetailUserModel.Empty;
            NumberOfSeats = null;


        }
    }
}
