using project.BL.Models;

namespace project.APP.Messages
{
    public record SelectedMessage<T> : Message<T>
        where T : IModel
    {
    }
}
