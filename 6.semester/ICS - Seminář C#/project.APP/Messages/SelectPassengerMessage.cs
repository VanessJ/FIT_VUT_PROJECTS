using project.BL.Models;

namespace project.APP.Messages
{
    public record SelectPassengerMessage<T> : Message<T>
        where T : IModel
    {
    }
}