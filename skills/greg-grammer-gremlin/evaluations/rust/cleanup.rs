pub fn nonempty(value: &str) -> bool {
    let mut length = value.len();
    if length > 0 {
        true
    } else {
        false
    }
}

pub fn owned_length(value: String) -> usize {
    let copied = value.clone();
    copied.len()
}
