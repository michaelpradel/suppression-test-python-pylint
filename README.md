# suppression-test-python-pylint

This repository is used to test our analysis code for studying suppressed warnings.
The focus here is on
 * Python repositories
 * the Pylint linter
 * the histories of individual suppressions

## Expected output of our analysis scripts

*TODO: Turn this into an automatically testable format, e.g., an expected JSON file*

* Suppression "disable=invalid-name"
  * Introduced in commit b8c363dab2c08061876d71b926f3cd4b0a5dd3a7
  * Code on same line changed in commit a2b8e1e9636bac9464ecbc1df48cccea228bff75
  * Removed in commit 6f794e03473ba9cfdcb7afcede0b4076055ae6da

* Suppression "disable=all"
  * Introduced in commit 2977797af18b6a74e72e6bb5d32d577016451311
  * Moved to another line (but suppression is not changed) in commit 023f64a4f4f4e82dde9221b5a2eb845bf2a85392
  * (Never removed)

* Suppression "disable=missing-module-docstring"
  * Introduced in a09fcfece6532e441c33be40c59d98c4623da3cf
  * Moved to another line (but suppression is not changed) in commit 125ad475f183d09959c522939063daa445829e30
  * File with suppression renamed (but suppression is not changed) in commit c6de5547789230ae91374b156643c76d8b4e2b9e
  * Moved to another line (but suppression is not changed) in commit 72a505d1ffcd08837699c99652006bbbd0736a7b