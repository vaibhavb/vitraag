# About
Homepage of Vaibhav Bhandari

# Next Item Todo List [Updated 05/29/2025]

## High Priority Technical Improvements
[x] **Remove Unused Build Tools**: Eliminate webpack, babel, and React dependencies since React is only used for a single unused finance component. The webpack bundle.js is only loaded in report.html but no React mount point exists.
[x] **Consolidate CSS Frameworks**: Remove redundant CSS frameworks - currently using Bulma, Tailwind, and Pico CSS simultaneously. Standardize on one framework (recommend keeping Bulma since it's actively used).
[] **Optimize Asset Pipeline**: Remove unnecessary Sass compilation steps and simplify the build process by eliminating unused theme files and webpack configuration.
[] **Clean Up Dependencies**: Update package.json to remove 15+ unused development dependencies including React, babel loaders, and webpack-related packages.
[] **Improve File Organization**: Move unused/legacy files to archive directories and consolidate scattered JavaScript files in assets/js and assets/webpack.

## Existing Todo Items
[] Feat: Add ability to generate review cards from content
[] Delete babel, tailwind and webpack
[] Fix images in all the blog files
[] Implement related posts by using embeddings based semantic similarity.
[] Re-org
    [] Refactor the react application to one area
    [] Refactor the code and move un-used pages to archive directory
[x] Open Questions
    [x] Is it possible to have multiple themes on the same homepage?
[] Editing
    [] Enable ability to write content in Notion, stage before creating a blogpost

# How to run?
```
npm run start
```

# Done List
[x] Add /books area
[x] Implement /travel page: its should have travels by year, category (location, hiking, climbing, motorcycle, etc.)
[x] Make sure you can view blogs by Month and then by Category
[x] Delete the nodes application

# Content List
[]
