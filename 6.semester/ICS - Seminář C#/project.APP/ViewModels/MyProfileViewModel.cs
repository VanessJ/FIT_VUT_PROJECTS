using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using project.APP.Commands;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;
using project.BL.Facade;
using project.BL.Models;

namespace project.APP.ViewModels
{
    public class MyProfileViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly UserFacade _userFacade;
        public MyProfileViewModel(IMediator mediator, UserFacade userFacade)
        {
            _mediator = mediator;
            _userFacade = userFacade;

            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(HidePage);
            _mediator.Register<ShowLookForRideMessege>(HidePage);
            _mediator.Register<ShowMyCarMessege>(HidePage);
            _mediator.Register<ShowMyProfileMessege>(ShowPage);
            _mediator.Register<ShowSettingsMessege>(HidePage);
            _mediator.Register<LogOutMessage>(HidePage);

            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);

            SaveCommand = new AsyncRelayCommand(SaveAsync, CanSave);
        }

        public ICommand SaveCommand { get; }

        private bool CanSave() => IsUserValid();

        private bool IsUserValid()
        {
            return (Model?.FirstName != string.Empty) && (Model?.LastName != string.Empty);
        }

        public async Task SaveAsync()
        {
            if (Model == null)
            {
                throw new InvalidOperationException("Null model cannot be saved");
            }

            Model = await _userFacade.SaveAsync(Model);
            _mediator.Send(new UsersUpdated());
        }

        private void ShowPage(ShowMyProfileMessege obj)
        {
            PageVisibility = Visibility.Visible;

        }

        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;

        }

        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadAsync(id);

        }

        public async Task LoadAsync(Guid id)
        {
            Model = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
        }


        public DetailUserModel? Model { get; set; } = DetailUserModel.Empty;

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;

    }
}
