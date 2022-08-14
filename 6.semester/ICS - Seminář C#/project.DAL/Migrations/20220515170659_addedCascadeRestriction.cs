using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace project.DAL.Migrations
{
    public partial class addedCascadeRestriction : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives",
                column: "DriverId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives",
                column: "DriverId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);
        }
    }
}
