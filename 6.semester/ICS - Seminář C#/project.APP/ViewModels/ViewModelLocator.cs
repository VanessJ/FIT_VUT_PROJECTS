
namespace project.APP.ViewModels;

 public class ViewModelLocator : ViewModelBase
{
    public ViewModelLocator()
    {
        TestViewModel = new TestViewModel();
    }

    public TestViewModel TestViewModel { get; }


    
}