use criterion::{black_box, criterion_group, criterion_main, Criterion};

const TEST_CRATE: &[u8] = include_wasm_rs::build_wasm!("wasm_module");

fn instantiate_base(bytes: &[u8]) {}
fn instantiate_crate(bytes: &[u8]) {}

fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("fib 20 BASE", |b| {
        b.iter(|| instantiate_base(black_box(TEST_CRATE)))
    });
    c.bench_function("fib 20 CRATE", |b| {
        b.iter(|| instantiate_crate(black_box(TEST_CRATE)))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
