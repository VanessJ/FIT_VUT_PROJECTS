using project.BL.Models;

namespace project.APP.Messages
{
    public record NewMessage<T> : Message<T>
        where T : IModel
    {
    }
}
