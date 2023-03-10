# perf-serve

Easily serve linux perf profile for firefox profiler.

# Usage

Just run `python3 -m perf_serve` in directory containing perf.data. That will run `perf script` and start serving resulting file on some free port. See `python3 -m perf_serve --help` for more usage information.

Due to https://github.com/firefox-devtools/profiler/issues/3766 it is currently impossible to load perf profiles from URL. While this issue is not fixed, perf-serve will default to using [profiler.forestryks.org](http://profiler.forestryks.org/), which is just hot-fixed version of firefox profiler

# Installation

`python3 -m pip install perf_serve`

Because _perf_serve_ serves a file via http, you need to set `Insecure content = Allow` in site options for [profiler.forestryks.org](http://profiler.forestryks.org/).
