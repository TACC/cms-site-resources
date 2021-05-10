# TACC CMS Per-Site Resources - Example - Static Files

All static files specific to this CMS project __must__ be placed here _within_ a directory whose name matches _the parent directory of this directory_. Failure to do so will make them unavailable via [Core CMS][core-cms-repo].

See [Core `static/README.md`](/taccsite_cms/static/README.md).


[core-cms-repo]: https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template


## Clarification

Where `cms-project-a` and `cms-project-b` are unique CMS projects with custom resources:

- `cms-site-resources:/cms-project-a/static/cms-project-a/…`
- `cms-site-resources:/cms-project-b/static/cms-project-b/…`

The redundancy is intentional. The high-level instance isolates per-project resources. The low-level instance [namespaces the custom static files and templates][djangocms-custom-resources].

[djangocms-custom-resources]: https://docs.djangoproject.com/en/2.2/intro/tutorial06/#customize-your-app-s-look-and-feel
