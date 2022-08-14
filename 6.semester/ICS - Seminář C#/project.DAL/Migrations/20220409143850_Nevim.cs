using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace project.DAL.Migrations
{
    public partial class Nevim : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cars_Users_UserEntityId",
                table: "Cars");

            migrationBuilder.DropIndex(
                name: "IX_Cars_UserEntityId",
                table: "Cars");

            migrationBuilder.DropColumn(
                name: "UserEntityId",
                table: "Cars");

            migrationBuilder.AddColumn<Guid>(
                name: "OwnerId",
                table: "Cars",
                type: "uniqueidentifier",
                nullable: false,
                defaultValue: new Guid("00000000-0000-0000-0000-000000000000"));

            migrationBuilder.CreateIndex(
                name: "IX_Cars_OwnerId",
                table: "Cars",
                column: "OwnerId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars",
                column: "OwnerId",
                principalTable: "Users",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cars_Users_OwnerId",
                table: "Cars");

            migrationBuilder.DropIndex(
                name: "IX_Cars_OwnerId",
                table: "Cars");

            migrationBuilder.DropColumn(
                name: "OwnerId",
                table: "Cars");

            migrationBuilder.AddColumn<Guid>(
                name: "UserEntityId",
                table: "Cars",
                type: "uniqueidentifier",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_Cars_UserEntityId",
                table: "Cars",
                column: "UserEntityId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cars_Users_UserEntityId",
                table: "Cars",
                column: "UserEntityId",
                principalTable: "Users",
                principalColumn: "Id");
        }
    }
}
