using project.BL.Models;

namespace project.APP.Messages
{
    public record AddedMessage<T> : Message<T>
        where T : IModel
    {
    }
}