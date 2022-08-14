using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
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
    public class LogOutViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        private readonly UserFacade _userFacade;


        public LogOutViewModel(IMediator mediator, UserFacade userFacade)
        {
            _userFacade = userFacade;
            _mediator = mediator;

            _mediator = mediator;
            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(HidePage);
            _mediator.Register<ShowLookForRideMessege>(HidePage);
            _mediator.Register<ShowMyCarMessege>(HidePage);
            _mediator.Register<ShowMyProfileMessege>(HidePage);
            _mediator.Register<ShowSettingsMessege>(HidePage);
            _mediator.Register<LogOutMessage>(ShowPage);
            _mediator.Register<UsersUpdated>(UpdateUserList);

            _mediator.Register<SelectedMessage<DetailUserModel>>(UpdateSelectedUser);


            SaveCommand = new AsyncRelayCommand(SaveAsync, CanSave);
            DeleteCommand = new AsyncRelayCommand(DeleteAsync, CanDelete);
            UserSelectedCommand = new RelayCommand<ListUserModel>(UserSelected);


            _mediator.Send(new UsersUpdated());

        }

        public async Task DeleteAsync()
        {
            if (Model is null)
            {
                throw new InvalidOperationException("Null model cannot be deleted");
            }

            await _userFacade.DeleteAsync(CurrentUserModel);
            _mediator.Send(new UsersUpdated());
            CurrentUserModel = DetailUserModel.Empty;
            _mediator.Send(new HideGridMenuMessage());
            SelectedUser = "To continue select an user";
            DeleteButtonVisibility = Visibility.Hidden;
        }

        private bool CanDelete() => IsUserSelected();

        private bool IsUserSelected()
        {
            return (CurrentUserModel?.Id != Guid.Empty);
        }


        private void UserSelected(ListUserModel? user) => _mediator.Send(new SelectedMessage<DetailUserModel> { Id = user?.Id });

        public ICommand SaveCommand { get; }
        public ICommand UserSelectedCommand { get; }

        public ICommand DeleteCommand { get; }

        public DetailUserModel? Model { get; set; } = DetailUserModel.Empty;


        public DetailUserModel? CurrentUserModel { get; set; } = DetailUserModel.Empty;

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;

        public Visibility DeleteButtonVisibility { get; set; } = Visibility.Hidden;
        public ObservableCollection<ListUserModel> Users { get; set; } = new();


        public string SelectedUser { get; set; } = "To continue select an user";



        private void ShowPage(LogOutMessage obj)
        {
            PageVisibility = Visibility.Visible;

        }

        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;

        }


        private async void UpdateUserList(UsersUpdated obj) => await LoadAsync();

        private async void UpdateSelectedUser(SelectedMessage<DetailUserModel> obj)
        {
            if (obj.Id == null) return;
            var id = obj.Id ?? Guid.Empty;
            await LoadAsync(id);
            SelectedUser = CurrentUserModel?.FirstName ?? string.Empty;
            if (CurrentUserModel.Id != Guid.Empty)
            {
                _mediator.Send(new ShowGridMenuMessege());
                DeleteButtonVisibility = Visibility.Visible;
            }
            
        }

        private bool CanSave() => IsUserValid();

        private bool IsUserValid()
        {
            return Model is { FirstName: { }, LastName: { } };
        }


        public async Task SaveAsync()
        {
            if (Model == null)
            {
                throw new InvalidOperationException("Null model cannot be saved");
            }

            Model = await _userFacade.SaveAsync(Model);
            _mediator.Send(new UsersUpdated());
            Model = DetailUserModel.Empty;
        }



        public async Task LoadAsync(Guid id)
        {
            CurrentUserModel = await _userFacade.GetAsync(id) ?? DetailUserModel.Empty;
        }


        public async Task LoadAsync()
        {
            Users.Clear();
            var users = await _userFacade.GetAsync();
            Users.AddRange(users);
        }

    }
}
