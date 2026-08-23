# Patterns d'implémentation par framework

Référence des patterns et snippets spécifiques à chaque framework cible.

## Table des matières

1. [React](#react)
2. [Vue](#vue)
3. [Angular](#angular)
4. [Vanilla HTML/CSS/JS](#vanilla)
5. [Patterns CSS universels](#patterns-css-universels)

---

## React

### Structure composant

```jsx
// Pattern : Composant avec variants
function Button({ variant = "primary", size = "md", children, ...props }) {
  return (
    <button className={`btn btn-${variant} btn-${size}`} {...props}>
      {children}
    </button>
  );
}
```

### Patterns layout

```jsx
// Grid responsive avec CSS Modules
<div className={styles.grid}>
  {items.map(item => (
    <Card key={item.id} data={item} />
  ))}
</div>
```

### State management pour UI

```jsx
// États d'interface courants
const [isLoading, setIsLoading] = useState(false);
const [activeTab, setActiveTab] = useState("overview");
const [isMenuOpen, setIsMenuOpen] = useState(false);
```

### Responsive patterns

```jsx
// Hook media query
function useMediaQuery(query) {
  const [matches, setMatches] = useState(
    () => window.matchMedia(query).matches
  );
  useEffect(() => {
    const mql = window.matchMedia(query);
    const handler = (e) => setMatches(e.matches);
    mql.addEventListener("change", handler);
    return () => mql.removeEventListener("change", handler);
  }, [query]);
  return matches;
}
```

---

## Vue

### Structure composant

```vue
<script setup>
// Pattern : Props avec defaults
const props = withDefaults(defineProps<{
  variant?: 'primary' | 'secondary'
  size?: 'sm' | 'md' | 'lg'
}>(), {
  variant: 'primary',
  size: 'md'
})
</script>

<template>
  <button :class="[`btn-${variant}`, `btn-${size}`]">
    <slot />
  </button>
</template>
```

### Reactive state

```vue
<script setup>
const isLoading = ref(false)
const activeTab = ref('overview')
const formData = reactive({ name: '', email: '' })
</script>
```

---

## Angular

### Structure composant

```typescript
// Pattern : Component avec Input/Output
@Component({
  selector: 'app-button',
  template: `
    <button [ngClass]="['btn', 'btn-' + variant, 'btn-' + size]">
      <ng-content></ng-content>
    </button>
  `
})
export class ButtonComponent {
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Input() size: 'sm' | 'md' | 'lg' = 'md';
  @Output() clicked = new EventEmitter<void>();
}
```

---

## Vanilla

### Structure HTML sémantique

```html
<header class="header">
  <nav class="nav" aria-label="Main navigation">
    <ul class="nav__list">
      <li class="nav__item nav__item--active">
        <a href="#" class="nav__link">Dashboard</a>
      </li>
    </ul>
  </nav>
</header>
<main class="content">
  <section class="section" aria-labelledby="section-title">
    <h2 id="section-title">Section Title</h2>
  </section>
</main>
```

### BEM naming convention

```css
.block {}
.block__element {}
.block--modifier {}
.block__element--modifier {}
```

---

## Patterns CSS universels

### Grid system

```css
/* Auto-responsive grid */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

/* Fixed columns avec breakpoints */
.grid-fixed {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
@media (max-width: 768px) {
  .grid-fixed { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
  .grid-fixed { grid-template-columns: 1fr; }
}
```

### Spacing system (8px base)

```css
:root {
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
}
```

### Shadow elevation system

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
  --shadow-xl: 0 20px 25px rgba(0,0,0,0.1);
}
```

### Typography scale

```css
:root {
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
}
```

### Responsive breakpoints courants

```css
/* Mobile first */
/* sm: 640px  — Petit mobile → grand mobile */
/* md: 768px  — Tablette portrait */
/* lg: 1024px — Tablette paysage / petit desktop */
/* xl: 1280px — Desktop */
/* 2xl: 1536px — Grand desktop */
```
