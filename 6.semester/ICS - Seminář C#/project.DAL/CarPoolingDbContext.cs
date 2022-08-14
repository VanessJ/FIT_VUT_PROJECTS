using System;
using project.DAL.Entities;
using project.DAL.Seeds;

using Microsoft.EntityFrameworkCore;

namespace project.DAL
{
	public  class CarPoolingDbContext : DbContext
	{	
		private readonly bool _seedDemoData;
		public CarPoolingDbContext(DbContextOptions contextOptions, bool seedDemoData = false) : base(contextOptions)
		{
			_seedDemoData = seedDemoData;		
		}
		
		public DbSet<CarEntity> Cars => Set<CarEntity>();
		public DbSet<DriveEntity> Drives => Set<DriveEntity>();
		public DbSet<UserEntity> Users => Set<UserEntity>();

		protected override void OnModelCreating(ModelBuilder modelBuilder)
		{
			base.OnModelCreating(modelBuilder);

			modelBuilder.Entity<CarEntity>()
				.HasMany(i => i.Drives)
				.WithOne(x => x.Car)
				.OnDelete(DeleteBehavior.Cascade);

			modelBuilder.Entity<DriveEntity>()
				.HasMany(x => x.Passengers)
				.WithOne()
				.OnDelete(DeleteBehavior.SetNull);
			modelBuilder.Entity<DriveEntity>()
				.HasOne(x => x.Driver)
				.WithMany()
				.OnDelete(DeleteBehavior.SetNull);

			modelBuilder.Entity<CarEntity>()
				.HasOne(i => i.Owner)
				.WithMany()
				.OnDelete(DeleteBehavior.SetNull);

			//modelBuilder.Entity<DriveEntity>()
			//	.HasOne(x => x.Driver)
			//	.WithOne()
			//	.OnDelete(DeleteBehavior.Restrict);

			if (_seedDemoData)
            {
				UserSeeds.Seed(modelBuilder);
				DriverSeeds.Seed(modelBuilder);
				CarSeeds.Seed(modelBuilder);
            }
		}
		
		
		

	}
}

