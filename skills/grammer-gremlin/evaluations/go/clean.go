package sample

// RecordBeforeAndAfter records the updated value first, then the original value.
func RecordBeforeAndAfter(record func(int), value int) {
	defer record(value)
	value++
	record(value)
}
