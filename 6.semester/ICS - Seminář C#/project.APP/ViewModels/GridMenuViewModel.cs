using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using Microsoft.Toolkit.Mvvm.Input;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;

namespace project.APP.ViewModels
{
    public class GridMenuViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        public GridMenuViewModel(IMediator mediator)
        {
            //prijme singleton mediatoru a priradi ho do lokalni promenne at s nim muzem tady pracovat
            _mediator = mediator;
            //registruje k prijmu zpravy "ShowMainPageMessage" a pokud ji to prijme, zavola se metoda ShowMainPage


            MainPageSelectedCommand = new RelayCommand(MainPageSelected);
            CreateNewRideSelectedCommand = new RelayCommand(CreateNewRideSelected);
            LookForRideCommand = new RelayCommand(LookForRideSelected);
            MyProfileSelectedCommand = new RelayCommand(MyProfileSelected);
            MyCarSelectedCommand = new RelayCommand(MyCarSelected);
            SettingsSelectedCommand = new RelayCommand(SettingsSelected);
            LogoutCommand = new RelayCommand(LogOutSelected);

            _mediator.Register<ShowGridMenuMessege>(ShowPage);
            _mediator.Register<HideGridMenuMessage>(HidePage);


        }

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;

        public ICommand MainPageSelectedCommand{ get; }

        public ICommand CreateNewRideSelectedCommand { get; }
        public ICommand LookForRideCommand { get; }

        public ICommand MyProfileSelectedCommand { get; }

        public ICommand MyCarSelectedCommand { get; }
        public ICommand SettingsSelectedCommand { get; }

        public ICommand LogoutCommand{ get; }

        private void ShowPage(ShowGridMenuMessege obj)
        {
            PageVisibility = Visibility.Visible;
        }

        private void HidePage(HideGridMenuMessage obj)
        {
            PageVisibility = Visibility.Hidden;

        }

        public void MainPageSelected()
        {
            _mediator.Send(new ShowMainPageMessage());
        }

        public void CreateNewRideSelected()
        {
            _mediator.Send(new ShowCreateNewRideMessege()); 
        }

        public void LookForRideSelected()
        {
            _mediator.Send(new ShowLookForRideMessege());
        }

        public void MyProfileSelected()
        {
            _mediator.Send(new ShowMyProfileMessege());
        }

        public void MyCarSelected()
        {
            _mediator.Send(new ShowMyCarMessege());
        }

        public void SettingsSelected()
        {
            _mediator.Send(new ShowSettingsMessege());
        }

        public void LogOutSelected()
        {
            _mediator.Send(new LogOutMessage());
        }


    }

}
