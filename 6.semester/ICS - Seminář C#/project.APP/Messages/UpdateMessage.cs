using project.BL.Models;

namespace project.APP.Messages
{
    public record UpdateMessage<T> : Message<T>
        where T : IModel
    {
    }
}
