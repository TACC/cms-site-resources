# TACC CMS Per-Site Resources - Example - Templates

All templates specific to this CMS project __must__ be placed in this directory. Failure to do so will make them unavailable via [Core CMS][core-cms-repo].

[core-cms-repo]: https://gitlab.tacc.utexas.edu/wma-cms/cms-site-template

## Page Templates

Projects may make templates available as page templates for CMS editors, via this directory, _similar_ to the Core. See [Core `templates/README.md` at "Page Templates"](/taccsite_cms/templates/README.md#Page%20Templates).

### Overwrite Core Templates

To overwrite Core templates, you may create a template of the same name within `./taccsite_cms` here, example: `__PROJECT__/templates/taccsite_cms/__TEMPLATE__.html`.

> __Important__: A project must __not__ overwrite the Core CMS `base.html`.

#### Backwards Compatibility

Some projects did not have this feature, so they registered their template in `_CMS_TEMPLATES` in `secrets.py`, i.e. `('__PROJECT__/templates/__TEMPLATE__.html', 'Template Name')`, and relied on the CMS admin to choose the correct template for every page. This will still work, but those websites should be updated to use the new automatic inheritence.

Steps to Update:

1. Copy `__PROJECT__/templates/__TEMPLATE__.html` template to  `__PROJECT__/templates/taccsite_cms/__TEMPLATE__.html`.
2. Reduce `__PROJECT__/templates/__TEMPLATE__.html` content to:

  ```twig
  {% extends "__PROJECT__/templates/taccsite_cms/__TEMPLATE__.html" %}
  ```

3. Test code change.
4. Deploy code change.
5. Update (via CMS admin) all pages using template `__PROJECT__/templates/__TEMPLATE__.html` to use `__TEMPLATE__.html`.
6. Delete `__PROJECT__/templates/__TEMPLATE__.html`.
7. Remove `('__PROJECT__/templates/__TEMPLATE__.html', 'Template Name')` from `_CMS_TEMPLATES` in `secrets.py`.
8. Ensure `('__TEMPLATE__.html', 'Template Name')` exists `_CMS_TEMPLATES` in `secrets.py`.

## Overwrite Apps or Plugins

Projects may overwrite apps/plugins, via this directory, just like the Core. See [Core `templates/README.md` at "Overwrite Plugins"](/taccsite_cms/templates/README.md#Overwrite%20or%20Plugins).
