using project.APP.Commands;
using project.APP.Services;
using project.APP.ViewModels;
using project.APP.Messages;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using project.App.Extensions;
using project.APP.Messages.ShowPageMesseges;
using project.APP.ViewModels.Interfaces;
using project.BL.Facade;
using project.BL.Models;

namespace project.APP.ViewModels
{
    public class MainWindowViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;




        public MainWindowViewModel(IMediator mediator, MainPageViewModel mainPageViewModel, GridMenuViewModel gridMenuViewModel, 
                                   CreateNewRideViewModel createNewRideViewModel, LookForRideViewModel lookForRideViewModel,
                                   MyCarViewModel myCarViewModel, MyProfileViewModel myProfileViewModel,
                                   SettingsViewModel settingsViewModel, LogOutViewModel logOutViewModel)
        {
            _mediator = mediator;

            _mediator.Register<ShowMainPageMessage>(MainPageSelected);
            _mediator.Register<ShowCreateNewRideMessege>(CreateNewRideSelected);
            _mediator.Register<ShowLookForRideMessege>(LookForRideSelected);
            _mediator.Register<ShowMyCarMessege>(MyCarSelected);
            _mediator.Register<ShowMyProfileMessege>(MyProfileSelected);
            _mediator.Register<ShowSettingsMessege>(SettingsSelected);
            _mediator.Register<LogOutMessage>(LogOutSelected);



            //vytvorime command, ktery vyvola poslani zpravy - ShowMainPage je metoda, ktera zpravu posle
            MainPageViewModel = mainPageViewModel;
            GridMenuViewModel = gridMenuViewModel;
            CreateNewRideViewModel = createNewRideViewModel;
            LookForRideViewModel = lookForRideViewModel;
            MyCarViewModel = myCarViewModel;    
            MyProfileViewModel = myProfileViewModel;
            LogOutViewModel = logOutViewModel;
            SettingsViewModel = settingsViewModel;

            _mediator.Send(new LogOutMessage());

        }

        private void MainPageSelected(IMessage obj)
        {
            CurrentPage = "Main Page";

        }

        private void CreateNewRideSelected(IMessage obj)
        {
            CurrentPage = "Create New Ride";

        }

        private void LookForRideSelected(IMessage obj)
        {
            CurrentPage = "Look For Ride";

        }

        private void MyCarSelected(IMessage obj)
        {
            CurrentPage = "My Car";

        }

        private void MyProfileSelected(IMessage obj)
        {
            CurrentPage = "My Profile";

        }

        private void SettingsSelected(IMessage obj)
        {
            CurrentPage = "Settings";

        }

        private void LogOutSelected(IMessage obj)
        {
            CurrentPage = "Log Out";

        }


        public CreateNewRideViewModel CreateNewRideViewModel { get; }
        public MainPageViewModel MainPageViewModel{ get; }
        
        public GridMenuViewModel GridMenuViewModel { get; }

        public  LookForRideViewModel LookForRideViewModel { get; }

        public MyCarViewModel MyCarViewModel { get; }

        public MyProfileViewModel MyProfileViewModel { get; }

        public SettingsViewModel SettingsViewModel { get; }

        public LogOutViewModel LogOutViewModel { get; }


        public string CurrentPage { get; set; } = "Test";
    }
}
