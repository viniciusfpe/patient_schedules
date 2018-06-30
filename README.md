# Patient Scheduling

Patient Scheduling System.

## Getting Started


### Prerequisites

```
Python 3.5
Virtualenv # http://virtualenvwrapper.readthedocs.io/en/latest/
```

### Installing

```
$ git clone https://github.com/viniciusfpe/patient_schedules.git
$ cd patient_schedules
$ make install # to install dependecies, migrate models and create super user
$ make runserver # to run project 
```

## Running the tests

```
$ make test # to run tests and get coverage
```

## Load test result

```
Requests/Seconds: 118.91
Requests/Minute: 7134.6
Response Time Min: 3.4ms
Response Time Max: 66.5ms

All virtual users finished
Summary report @ 13:51:27(-0300) 2018-06-30
  Scenarios launched:  7200
  Scenarios completed: 7200
  Requests completed:  7200
  RPS sent: 118.91
  Request latency:
    min: 3.4
    max: 66.5
    median: 3.9
    p95: 7
    p99: 19.8
  Scenario counts:
    0: 7200 (100%)
  Codes:
    200: 7200
```

For the load test artillery-io was used

#### Prerequisites to load test
```
Node version v8.9^
NPM version v5.6
``` 
#### Install artillery.io

```
$ npm install -g artillery
```

#### Run load test

```
$ make artillery
```

## Authors

* **Vinicius Peixoto** - *Initial work* - [Patient Schedules](https://github.com/viniciusfpe/patient_schedules)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
