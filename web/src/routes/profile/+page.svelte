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

	const levels = ['junior', 'mid', 'senior', 'staff', 'principal'];

	async function loadExisting() {
		if (!activeProfile.id) return;
		try {
			const p = await api.getProfile(activeProfile.id);
			loaded = p;
			name = p.name;
			skillsText = (p.skills ?? []).join(', ');
			yearsExperience = p.years_experience ?? '';
			currentLevel = p.current_level ?? 'mid';
			targetRolesText = (p.target_roles ?? []).join(', ');
		} catch (e) {
			error = e.message;
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
