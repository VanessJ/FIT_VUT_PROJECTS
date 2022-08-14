using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace project.DAL.Migrations
{
    public partial class nazev : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives",
                column: "CarId",
                principalTable: "Cars",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives",
                column: "DriverId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives",
                column: "CarId",
                principalTable: "Cars",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives",
                column: "DriverId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
