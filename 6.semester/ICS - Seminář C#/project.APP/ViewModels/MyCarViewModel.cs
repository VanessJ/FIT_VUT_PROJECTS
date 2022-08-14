using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Input;
using project.APP.Commands;
using project.App.Extensions;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;
using project.BL.Facade;
using project.BL.Models;

namespace project.APP.ViewModels
{
    public class MyCarViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly UserFacade _userFacade;
       
        private readonly CarFacade _carFacade;
        public MyCarViewModel(IMediator mediator, UserFacade userFacade, CarFacade carFacade)
        {
            //prijme singleton mediatoru a priradi ho do lokalni promenne at s nim muzem tady pracovat
            _mediator = mediator;
            _userFacade = userFacade;
            _carFacade = carFacade;

            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(HidePage);
            _mediator.Register<ShowLookForRideMessege>(HidePage);
            _mediator.Register<ShowMyCarMessege>(ShowPage);
            _mediator.Register<ShowMyProfileMessege>(HidePage);
            _mediator.Register<ShowSettingsMessege>(HidePage);
            _mediator.Register<LogOutMessage>(HidePage);

            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);
            _mediator.Register<CarsUpdated>(UpdateCarList);
            _mediator.Register<SelectedMessage<DetailCarModel>>(UpdateSelectedCar);


            SaveCommand = new AsyncRelayCommand(SaveAsync, CanSave);
            EditCommand = new AsyncRelayCommand(EditAsync, CanEdit);
            DeleteCommand = new AsyncRelayCommand(DeleteAsync, CanDelete);
            CarSelectedCommand = new RelayCommand<ListCarModel>(CarSelected);
        }


        public async Task DeleteAsync()
        {
            if (SelectedCarModel is null)
            {
                throw new InvalidOperationException("Null model cannot be deleted");
            }

            await _carFacade.DeleteAsync(SelectedCarModel);
            _mediator.Send(new CarsUpdated());
            SelectedCarModel = DetailCarModel.Empty;
            DetailVisibility = Visibility.Hidden;
        }

        public async Task SaveAsync()
        {
            if (NewCarModel == null)
            {
                throw new InvalidOperationException("Null model cannot be saved");
            }

            NewCarModel.OwnerId = User.Id;
            NewCarModel = await _carFacade.SaveAsync(NewCarModel);

            _mediator.Send(new CarsUpdated());
            NewCarModel = new DetailCarModel();
        }



        public async Task EditAsync()
        {
            if (SelectedCarModel == null)
            {
                throw new InvalidOperationException("Null model cannot be saved");
            }
            
            SelectedCarModel = await _carFacade.SaveAsync(SelectedCarModel);
            _mediator.Send(new CarsUpdated());
        }

        private void CarSelected(ListCarModel? car) => _mediator.Send(new SelectedMessage<DetailCarModel> { Id = car?.Id });
        private bool CanSave() => IsModelValid(NewCarModel);

        private bool CanDelete() => IsCarValid();



        private bool CanEdit() => IsCarValid();


        private bool IsCarValid()
        {
            return (SelectedCarModel?.Manufacturer != string.Empty) && (SelectedCarModel?.Type != string.Empty);
        }

        private bool IsModelValid(DetailCarModel? model)
        {
            return model is { Manufacturer: { }, Type: { }};
        }

        public ICommand SaveCommand { get; }
        public ICommand EditCommand { get; }

        public ICommand DeleteCommand{ get; }

        public ICommand CarSelectedCommand { get; }
        public Visibility PageVisibility { get; set; } = Visibility.Hidden;

        public Visibility DetailVisibility{ get; set; } = Visibility.Hidden;


        public ObservableCollection<ListCarModel> Cars { get; set; } = new();
        private void ShowPage(ShowMyCarMessege obj)
        {
            PageVisibility = Visibility.Visible;

        }

        public DetailCarModel? NewCarModel{ get; set; } = DetailCarModel.Empty;

        public DetailCarModel? SelectedCarModel { get; set; } = DetailCarModel.Empty;
        public DetailUserModel? User { get; set; } = DetailUserModel.Empty;


        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;
            SelectedCarModel = DetailCarModel.Empty;
            DetailVisibility  = Visibility.Hidden;
            
            

        }

        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadAsync(id);
            _mediator.Send(new CarsUpdated()); 

        }

        private async void UpdateSelectedCar(SelectedMessage<DetailCarModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadCarAsync(id);
            _mediator.Send(new CarsUpdated());
            DetailVisibility = Visibility.Visible;
        }

        private async void UpdateCarList(CarsUpdated obj) => await LoadAsync();


        public async Task LoadCarAsync(Guid id)
        {
            SelectedCarModel = await _carFacade.GetAsync(id) ?? DetailCarModel.Empty;
        }


        public async Task LoadAsync(Guid id)
        {
            User = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
        }

        public async Task LoadAsync()
        {
            Cars.Clear();
            var cars =  _carFacade.GetCarsOfDriver(User.Id);
            Cars.AddRange(cars);
        }
    }
}
