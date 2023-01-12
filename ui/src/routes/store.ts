import { writable } from 'svelte/store';

export const strike = writable(0);
export const exit = writable(0);
export const notional = writable(0);
export const optionType = writable('call');

export const startDate = writable(today());
export const endDate = writable(today());
export const data = writable([]);
export const stats = writable({});

function today() {
	const date = new Date();
	const year = date.getFullYear();

	let month = (1 + date.getMonth()).toString();
	month = month.length > 1 ? month : '0' + month;

	let day = date.getDate().toString();
	day = day.length > 1 ? day : '0' + day;

	return `${year}-${month}-${day}`;
}
