using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace project.DAL.Migrations
{
    public partial class Myplans : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_UserEntityId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_UserEntityId1",
                table: "Drives");

            migrationBuilder.DropIndex(
                name: "IX_Drives_UserEntityId",
                table: "Drives");

            migrationBuilder.DropIndex(
                name: "IX_Drives_UserEntityId1",
                table: "Drives");

            migrationBuilder.DropColumn(
                name: "UserEntityId",
                table: "Drives");

            migrationBuilder.DropColumn(
                name: "UserEntityId1",
                table: "Drives");

            migrationBuilder.AddColumn<Guid>(
                name: "CarId",
                table: "Drives",
                type: "uniqueidentifier",
                nullable: false,
                defaultValue: new Guid("00000000-0000-0000-0000-000000000000"));

            migrationBuilder.AddColumn<Guid>(
                name: "DriverId",
                table: "Drives",
                type: "uniqueidentifier",
                nullable: false,
                defaultValue: new Guid("00000000-0000-0000-0000-000000000000"));

            migrationBuilder.CreateTable(
                name: "DriveEntityUserEntity",
                columns: table => new
                {
                    DrivesAsPassengerId = table.Column<Guid>(type: "uniqueidentifier", nullable: false),
                    PassengersId = table.Column<Guid>(type: "uniqueidentifier", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_DriveEntityUserEntity", x => new { x.DrivesAsPassengerId, x.PassengersId });
                    table.ForeignKey(
                        name: "FK_DriveEntityUserEntity_Drives_DrivesAsPassengerId",
                        column: x => x.DrivesAsPassengerId,
                        principalTable: "Drives",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_DriveEntityUserEntity_Users_PassengersId",
                        column: x => x.PassengersId,
                        principalTable: "Users",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_Drives_CarId",
                table: "Drives",
                column: "CarId");

            migrationBuilder.CreateIndex(
                name: "IX_Drives_DriverId",
                table: "Drives",
                column: "DriverId");

            migrationBuilder.CreateIndex(
                name: "IX_DriveEntityUserEntity_PassengersId",
                table: "DriveEntityUserEntity",
                column: "PassengersId");

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
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.DropTable(
                name: "DriveEntityUserEntity");

            migrationBuilder.DropIndex(
                name: "IX_Drives_CarId",
                table: "Drives");

            migrationBuilder.DropIndex(
                name: "IX_Drives_DriverId",
                table: "Drives");

            migrationBuilder.DropColumn(
                name: "CarId",
                table: "Drives");

            migrationBuilder.DropColumn(
                name: "DriverId",
                table: "Drives");

            migrationBuilder.AddColumn<Guid>(
                name: "UserEntityId",
                table: "Drives",
                type: "uniqueidentifier",
                nullable: true);

            migrationBuilder.AddColumn<Guid>(
                name: "UserEntityId1",
                table: "Drives",
                type: "uniqueidentifier",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_Drives_UserEntityId",
                table: "Drives",
                column: "UserEntityId");

            migrationBuilder.CreateIndex(
                name: "IX_Drives_UserEntityId1",
                table: "Drives",
                column: "UserEntityId1");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_UserEntityId",
                table: "Drives",
                column: "UserEntityId",
                principalTable: "Users",
                principalColumn: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_UserEntityId1",
                table: "Drives",
                column: "UserEntityId1",
                principalTable: "Users",
                principalColumn: "Id");
        }
    }
}
