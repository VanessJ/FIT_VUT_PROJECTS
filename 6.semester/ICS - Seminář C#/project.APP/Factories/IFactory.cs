namespace project.APP.Factories
{
    public interface IFactory<out T>
    {
        T Create();
    }
}