export const meta = {
  name: 'example-workflow',
  description: 'Orchestration multi-agents. Supprimer si le plugin n en fournit pas.',
  phases: [{ title: 'Analyse' }],
}

phase('Analyse')
const result = await agent('Decrire la tache confiee au sous-agent.')
return { result }
