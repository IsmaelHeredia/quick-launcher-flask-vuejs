const backend_url = '/api';
const session_name = 'quick_launcher_session';

axios.defaults.headers.common = { 'Authorization': `Bearer ${sessionStorage.getItem(session_name)}` }