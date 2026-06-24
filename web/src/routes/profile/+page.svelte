<script>
	import { api } from '$lib/api.js';
	import { activeProfile, setActiveProfile } from '$lib/profile.svelte.js';

	let name = $state('');
	let skillsText = $state('');
	let yearsExperience = $state('');
	let currentLevel = $state('mid');
	let targetRolesText = $state('');

	let saving = $state(false);
	let error = $state('');
	let loaded = $state(null);

	let resumeFile = $state(null);
	let parsing = $state(false);
	let parsedNote = $state('');

	const levels = ['junior', 'mid', 'senior', 'staff', 'principal'];

	function populate(p) {
		loaded = p;
		name = p.name ?? '';
		skillsText = (p.skills ?? []).join(', ');
		yearsExperience = p.years_experience ?? '';
		currentLevel = p.current_level ?? 'mid';
		targetRolesText = (p.target_roles ?? []).join(', ');
	}

	async function loadExisting() {
		if (!activeProfile.id) return;
		try {
			populate(await api.getProfile(activeProfile.id));
		} catch (e) {
			error = e.message;
		}
	}

	async function uploadResume() {
		if (!resumeFile) return;
		parsing = true;
		error = '';
		parsedNote = '';
		try {
			const profile = await api.createProfileFromResume(resumeFile);
			setActiveProfile(profile.id);
			populate(profile);
			parsedNote = `Parsed "${resumeFile.name}" — review below, then see your matches on Jobs.`;
		} catch (e) {
			error = e.message;
		} finally {
			parsing = false;
		}
	}

	function parseList(text) {
		return text
			.split(',')
			.map((s) => s.trim())
			.filter(Boolean);
	}

	async function save() {
		saving = true;
		error = '';
		try {
			const profile = await api.createProfile({
				name,
				skills: parseList(skillsText),
				years_experience: yearsExperience ? Number(yearsExperience) : null,
				current_level: currentLevel,
				target_roles: parseList(targetRolesText)
			});
			setActiveProfile(profile.id);
			loaded = profile;
		} catch (e) {
			error = e.message;
		} finally {
			saving = false;
		}
	}

	function clearProfile() {
		setActiveProfile(null);
		loaded = null;
		name = '';
		skillsText = '';
		yearsExperience = '';
		currentLevel = 'mid';
		targetRolesText = '';
	}

	$effect(() => {
		loadExisting();
	});
</script>

<h1>Your profile</h1>
<p class="muted">
	LevelMatch compares this profile against each job posting to compute your match.
</p>

<div class="upload">
	<div class="upload-head">
		<strong>Upload a resume</strong>
		<span class="muted">PDF or text — we parse it into your profile</span>
	</div>
	<div class="upload-row">
		<input
			type="file"
			accept=".pdf,.txt,.md,text/plain,application/pdf"
			onchange={(e) => (resumeFile = e.currentTarget.files?.[0] ?? null)}
		/>
		<button onclick={uploadResume} disabled={!resumeFile || parsing}>
			{parsing ? 'Parsing…' : 'Parse resume'}
		</button>
	</div>
	{#if parsedNote}<p class="ok">{parsedNote}</p>{/if}
</div>

<p class="divider"><span>or edit manually</span></p>

<div class="form">
	<label>
		Name
		<input bind:value={name} placeholder="Job Seeker" />
	</label>

	<label>
		Skills <span class="muted">(comma-separated)</span>
		<textarea bind:value={skillsText} rows="3" placeholder="Python, SQL, RAG, FastAPI"></textarea>
	</label>

	<div class="row">
		<label>
			Years experience
			<input bind:value={yearsExperience} type="number" min="0" placeholder="4" />
		</label>
		<label>
			Current level
			<select bind:value={currentLevel}>
				{#each levels as level}<option value={level}>{level}</option>{/each}
			</select>
		</label>
	</div>

	<label>
		Target roles <span class="muted">(comma-separated)</span>
		<input bind:value={targetRolesText} placeholder="AI Engineer, ML Engineer" />
	</label>

	{#if error}<p class="error">{error}</p>{/if}

	<div class="actions">
		<button onclick={save} disabled={saving || !name}>
			{saving ? 'Saving…' : activeProfile.id ? 'Save as new profile' : 'Create profile'}
		</button>
		{#if activeProfile.id}
			<button class="secondary" onclick={clearProfile}>Clear active</button>
		{/if}
	</div>

	{#if loaded}
		<p class="ok">Active profile: <code>{loaded.id}</code></p>
	{/if}
</div>

<style>
	.upload {
		max-width: 540px;
		margin-top: 1.5rem;
		padding: 1rem 1.25rem;
		background: #161b22;
		border: 1px solid #30363d;
		border-radius: 10px;
	}
	.upload-head {
		display: flex;
		flex-direction: column;
		gap: 0.15rem;
		margin-bottom: 0.75rem;
	}
	.upload-row {
		display: flex;
		gap: 0.75rem;
		align-items: center;
	}
	.upload-row input[type='file'] {
		flex: 1;
		font-size: 0.85rem;
		color: #c9d1d9;
	}
	.divider {
		max-width: 540px;
		text-align: center;
		border-bottom: 1px solid #21262d;
		line-height: 0.1em;
		margin: 1.75rem 0 0.5rem;
	}
	.divider span {
		background: #0d1117;
		padding: 0 0.75rem;
		color: #8b949e;
		font-size: 0.85rem;
	}
	.form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		max-width: 540px;
		margin-top: 1.5rem;
	}
	label {
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
		font-weight: 600;
		font-size: 0.9rem;
	}
	.row {
		display: flex;
		gap: 1rem;
	}
	.row label {
		flex: 1;
	}
	input,
	textarea,
	select {
		padding: 0.55rem 0.7rem;
		background: #0d1117;
		border: 1px solid #30363d;
		border-radius: 6px;
		color: #e6edf3;
		font-size: 0.95rem;
		font-family: inherit;
	}
	.actions {
		display: flex;
		gap: 0.75rem;
	}
	button {
		padding: 0.6rem 1rem;
		background: #238636;
		border: none;
		border-radius: 6px;
		color: white;
		font-weight: 600;
		cursor: pointer;
	}
	button:disabled {
		opacity: 0.6;
		cursor: default;
	}
	button.secondary {
		background: #21262d;
		color: #e6edf3;
	}
	.muted {
		color: #8b949e;
		font-weight: 400;
	}
	.error {
		color: #f85149;
	}
	.ok {
		color: #4ac26b;
		font-size: 0.9rem;
	}
	code {
		background: #161b22;
		padding: 0.1rem 0.4rem;
		border-radius: 4px;
		font-size: 0.85rem;
	}
</style>
