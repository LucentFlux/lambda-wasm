# Lambda Wasm
A WebAssembly runtime with opinionated optimisations for very short-lived instances of known modules.

## Motivation

Creating an instance of a WebAssembly module is costly - at the very least, some memory must be allocated (usually via `mmap` calls), which is then deallocated when the module is finished being used. If you want to use WebAssembly modules as lambdas - isolated from other invocations of the same module - then you must incur this allocation and de-allocation penalty for every call.

Going back and forth between a WebAssembly module on Web is also costly, as every call must be performed through the JavaScript boundary. If you know the number and shape of the modules that you will be loading ahead of time, then you can skip the JS tax by statically linking your host WASM app with the modules that you want to use.

This crate does both of these things.

## Performance

| Benchmark | Base (Web) | λ-Wasm (Web) | Base (Native) | λ-Wasm (Native) |
| --- | ---: | ---: | ---: | ---: |
| fib 20 | 24658ns | 25300ns | 14128ns | 13934ns |

## Features

- [ ] Static module linking on web
- [ ] Module resetting
- [ ] Module pools