import { writable } from 'svelte/store';
import  old_data  from "./data"

export const strike = writable(0);
export const exit = writable(0);
export const notional = writable(0);
export const optionType = writable('call');

export const startDate = writable(today());
export const endDate = writable(today());
// export const data = writable([]);
// export const stats = writable({});

export const data = writable(old_data.results);
export const stats = writable(old_data.summary);
function today() {
	const date = new Date();
	const year = date.getFullYear();

	let month = (1 + date.getMonth()).toString();
	month = month.length > 1 ? month : '0' + month;

	let day = date.getDate().toString();
	day = day.length > 1 ? day : '0' + day;

	return `${year}-${month}-${day}`;
}
