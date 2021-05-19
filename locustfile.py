from locust import HttpUser, between, task, tag


class ESGFUser(HttpUser):
    host = "http://esgf3.dkrz.de"
    wait_time = between(5, 15)

    @tag("catalog")
    @task
    def catalog(self):
        query = "/thredds/catalog/catalog.html"

        with self.client.get(query, catch_response=True, name="catalog") as response:
            if "Earth System Root catalog" not in response.text:
                response.failure("Catalog response not as expected")

    # @tag("cmip5")
    # @task
    # def cmip5(self):
    #     query = "/thredds/fileServer/cmip5/cmip5/output1/MPI-M/MPI-ESM-LR/decadal1960/mon/atmos/Amon/r1i1p1/v20120529/tas/tas_Amon_MPI-ESM-LR_decadal1960_r1i1p1_196101-199012.nc"
    #     self.client.head(query, catch_response=True, name="cmip5")

    @tag("cmip6")
    @task
    def cmip6(self):
        query = "/thredds/fileServer/cmip6/CMIP/MPI-M/MPI-ESM1-2-LR/historical/r1i1p1f1/Amon/tas/gn/v20190710/tas_Amon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_185001-186912.nc"
        with self.client.head(query, catch_response=True, name="cmip6") as response:
            if "application/x-netcdf" not in response.headers['Content-Type']:
                response.failure("cmip6 response not as expected")
