export default function getListStudentIds(students) {
	if (!Array.isArray(students)) {
		return [];
	}

	const ids = students.map((item) => item.ids)
	
	return ids
}
