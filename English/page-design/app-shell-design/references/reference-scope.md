# Reference scope and sources

Read when adopting the supplied pattern, checking a framework claim, or attributing design evidence. Checked on 2026-11-14; consult the installed version before copying an API.

## Adopted brief

The user supplied this direction:

> UI shell layout follows Ant Design Pro layout specification: fixed left sidebar, top header, breadcrumb navigation above page content area.

Operationally, this means a collapsible left navigation that stays in place, a global top header, breadcrumb location, and a right content region with independent vertical scrolling. Use it for compatible new shells or when the task adopts this reference. Existing product structure and explicit scope remain authoritative.

This is a user-selected composition. Ant Design Pro offers configurable layouts; the quoted brief does not establish one compulsory configuration for every Ant application. The right-content scroll model is supplied by the user, not inferred from a screenshot or claimed as an official universal requirement.

## Sources and what they support

| Source | Supported use | Boundary |
| --- | --- | --- |
| [Ant Design Pro / ProLayout](https://procomponents.ant.design/en-US/components/layout/) and [official default settings](https://github.com/ant-design/ant-design-pro/blob/master/config/defaultSettings.ts) | Layout family, menu/breadcrumb integration, configurable layout and fixed regions | Defaults and option names depend on version; do not transplant configuration blindly |
| [Arco Design Pro layout source](https://github.com/arco-design/arco-design-pro/blob/main/arco-design-pro-vite/src/layout.tsx) | A concrete composition of Navbar, Sider, route-derived navigation, Breadcrumb, and Content | Reference for structure; no claim that every Arco product uses the same scrolling or theme |
| [Next.js layouts and pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages) | Shared layouts around route content | “Next.js Admin” does not identify a unique visual specification or package |

No upstream source code, logo, image, or theme is bundled here. This skill derives reusable decisions from the user's brief and public documentation.

## Evidence labels

- **User requirement:** the selected composition and independent right-content scrolling.
- **Observed/documented:** facts verified in supplied materials, official documentation, source code, or a running implementation; name which.
- **Estimated:** values inferred from a visual reference, with the uncertainty retained.
- **Supplemental design:** decisions needed to complete the task but absent from the reference, such as keyboard behavior, mobile navigation, return restoration, widths, and tokens.

The present reference is textual. There are no measured screenshot dimensions or observed interactive states. Choose and test missing details for the target product; a demo's values do not become cluster defaults.
