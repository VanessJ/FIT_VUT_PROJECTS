using System;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests;
using Xunit;
using Xunit.Abstractions;

namespace project.DAL.Tests
{
	// IAsyncLifetime ... we can use asynchronous calling in our tests ... InitializeAsync() and DisposeAsync()
	public class DbContextTestsBase : IAsyncLifetime
	{
		// tests are parallel and the console is static, so we could not distinguish which data are from which test
		// so instead into the console we are writing them to tne output helper
		protected DbContextTestsBase(ITestOutputHelper output)
		{
			XUnitTestOutputConverter converter = new(output);
			Console.SetOut(converter);

			DbContextFactory = new DbContextSqLiteTestingFactory(GetType().FullName!, seedTestingData: true);
			
			CarPoolingDbContextSUT= DbContextFactory.CreateDbContext();
		}

		protected IDbContextFactory<CarPoolingDbContext> DbContextFactory { get; }
		// SUT - system under test
		protected CarPoolingDbContext CarPoolingDbContextSUT { get; }


		public async Task InitializeAsync()
		{
			await CarPoolingDbContextSUT.Database.EnsureDeletedAsync();
			await CarPoolingDbContextSUT.Database.EnsureCreatedAsync();
		}

		public async Task DisposeAsync()
		{
			await CarPoolingDbContextSUT.Database.EnsureDeletedAsync();
			await CarPoolingDbContextSUT.DisposeAsync();
		}
	}
}
