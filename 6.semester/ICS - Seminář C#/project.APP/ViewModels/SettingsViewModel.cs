using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using project.APP.Messages;
using project.APP.Messages.ShowPageMesseges;
using project.APP.Services;

namespace project.APP.ViewModels
{
    public class SettingsViewModel : ViewModelBase
    {
        private readonly IMediator _mediator;
        public SettingsViewModel(IMediator mediator)
        {

            _mediator = mediator;
            _mediator.Register<ShowMainPageMessage>(HidePage);
            _mediator.Register<ShowCreateNewRideMessege>(HidePage);
            _mediator.Register<ShowLookForRideMessege>(HidePage);
            _mediator.Register<ShowMyCarMessege>(HidePage);
            _mediator.Register<ShowMyProfileMessege>(HidePage);
            _mediator.Register<ShowSettingsMessege>(ShowPage);
            _mediator.Register<LogOutMessage>(HidePage);

        }

        public Visibility PageVisibility { get; set; } = Visibility.Hidden;
        private void ShowPage(ShowSettingsMessege obj)
        {
            PageVisibility = Visibility.Visible;

        }

        private void HidePage(IMessage obj)
        {
            PageVisibility = Visibility.Hidden;

        }


    }
}
