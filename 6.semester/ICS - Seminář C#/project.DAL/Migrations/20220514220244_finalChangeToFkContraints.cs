using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace project.DAL.Migrations
{
    public partial class finalChangeToFkContraints : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.DropTable(
                name: "DriveEntityUserEntity");

            migrationBuilder.AddColumn<Guid>(
                name: "DriveEntityId",
                table: "Users",
                type: "uniqueidentifier",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_Users_DriveEntityId",
                table: "Users",
                column: "DriveEntityId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars",
                column: "OwnerId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);

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
                onDelete: ReferentialAction.SetNull);

            migrationBuilder.AddForeignKey(
                name: "FK_Users_Drives_DriveEntityId",
                table: "Users",
                column: "DriveEntityId",
                principalTable: "Drives",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives");

            migrationBuilder.DropForeignKey(
                name: "FK_Users_Drives_DriveEntityId",
                table: "Users");

            migrationBuilder.DropIndex(
                name: "IX_Users_DriveEntityId",
                table: "Users");

            migrationBuilder.DropColumn(
                name: "DriveEntityId",
                table: "Users");

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
                name: "IX_DriveEntityUserEntity_PassengersId",
                table: "DriveEntityUserEntity",
                column: "PassengersId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars",
                column: "OwnerId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Cars_CarId",
                table: "Drives",
                column: "CarId",
                principalTable: "Cars",
                principalColumn: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_Drives_Users_DriverId",
                table: "Drives",
                column: "DriverId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
