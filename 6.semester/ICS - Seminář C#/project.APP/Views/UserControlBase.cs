using System.Threading.Tasks;
using project.APP.ViewModels;
using System.Windows;
using System.Windows.Controls;
using project.APP.ViewModels.Interfaces;

namespace project.APP.Views
{
    public abstract class UserControlBase : UserControl
    {
        protected UserControlBase()
        {
            Loaded += OnLoaded;
        }

        private async void OnLoaded(object sender, RoutedEventArgs e)
        {
            if (DataContext is IListViewModel viewModel)
            {
                await viewModel.LoadAsync();
            }
        }
    }
}
