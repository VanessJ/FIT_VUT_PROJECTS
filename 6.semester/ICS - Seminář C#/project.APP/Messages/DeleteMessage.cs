using project.BL.Models;

namespace project.APP.Messages
{
    public record DeleteMessage<T> : Message<T>
        where T : IModel
    {
    }
}