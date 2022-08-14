using project.BL.Models;

namespace project.APP.Messages
{
    public record SelectedRideDetailMessage<T> : Message<T>
        where T : IModel
    {
    }
}