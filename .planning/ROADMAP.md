# Roadmap: HiveSec Ecosystem Hub

## Overview

The HiveSec Ecosystem Hub matures from a prototype dashboard to a full-featured security operations platform with robust agent orchestration, visualization, and integration capabilities.

## Phases

- [ ] **Phase 1: Stability** - Tests, CI, session state, error handling
- [ ] **Phase 2: Agents** - Plug new detectors, configure launches, manage credentials
- [ ] **Phase 3: Results** - Advanced filtering, export formats, correlation
- [ ] **Phase 4: Integrations** - Jira, GitHub Issues, Slack notifications
- [ ] **Phase 5: enterprise** - RBAC, audit logging, multi-tenancy

## Phase Details

### Phase 1: Stability
**Goal**: Make the dashboard reliable and production-ready
**Depends on**: None
**Requirements**: REQ-01 through REQ-04
**Success Criteria**:
  1. All pages load without errors under normal use
  2. CI runs tests and streamlit health check on PRs
  3. Session persistence across page reloads
  4. Clear error messages when agents fail
  5. Contributing and security docs published
**Plans**: 4 plans

Plans:
- [ ] 01-01: Add unit tests for agent orchestration module
- [ ] 01-02: Configure CI (pytest + streamlit)
- [ ] 01-03: Implement Streamlit session state management
- [ ] 01-04: Add global exception handler with user-friendly messages

### Phase 2: Agents
**Goal**: Expand the catalog of supported security agents
**Depends on**: Phase 1
**Success Criteria**:
  1. Agent registry allows dynamic registration of new detectors
  2. Credentials per agent stored securely (st.secrets)
  3. Ability to run agents concurrently (async)
  4. Agent output conforms to common finding schema
**Plans**: TBD

### Phase 3: Results
**Goal**: Improved analysis and export capabilities
**Depends on**: Phase 2
**Success Criteria**:
  1. Table view with filtering, sorting, pagination
  2. Charts: severity distribution, top categories
  3. Export to CSV, JSON, and PDF reports
  4. Correlation of findings across scans
**Plans**: TBD

### Phase 4: Integrations
**Goal**: Connect to external ticketing and notification systems
**Depends on**: Phase 3
**Success Criteria**:
  1. Create Jira issues from selected findings
  2. Open GitHub Issues in target repos
  3. Send Slack/Telegram alerts on critical findings
**Plans**: TBD

### Phase 5: Enterprise
**Goal**: Multi-user, team-ready features
**Depends on**: Phase 4
**Success Criteria**:
  1. Role-based access control (admin, analyst, readonly)
  2. Comprehensive audit logging
  3. Multi-tenant data isolation (optional)
**Plans**: TBD

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Stability | 0/4 | Not started | - |
| 2. Agents | 0 | Not started | - |
| 3. Results | 0 | Not started | - |
| 4. Integrations | 0 | Not started | - |
| 5. Enterprise | 0 | Not started | - |

---

*Roadmap will be refined during planning.*