---
name: move-github-issue
description: Explains how to move a GitHub issue to a different status column on a project board (v2) using the gh CLI. Use when you need to update an issue's status on a project board.
---

# How to Move an Issue on a GitHub Project Board

This guide provides the step-by-step process for changing an issue's status on a GitHub Project Board (also known as Projects V2) using the `gh` command-line interface.

## Prerequisites

- You need the `gh` CLI installed and authenticated.
- You need a GitHub token with `project` scope. This guide assumes it is stored in an environment variable like `$GH_TOKEN_PROJECTS`.
- You need to know the **Project Number** and the **Issue Number**.

## The Process

The process involves three main steps:
1.  Find the ID for the **Project Item**.
2.  Find the IDs for the **Status Field** and the target **Status Option** (e.g., "In Progress", "Done").
3.  Execute the `gh project item-edit` command.

---

### Step 1: Find the Project Item ID

A Project **Item** is the card on the board that represents your issue. You need its unique global ID.

- **Project Number**: The number of your project (e.g., `3` for `users/YOUR_USER/projects/3`).
- **Issue Number**: The number of the issue (e.g., `42` for `#42`).

Run this command, replacing `<PROJECT_NUMBER>` and `<ISSUE_NUMBER>`:

```bash
ITEM_ID=$(GH_TOKEN=$GH_TOKEN_PROJECTS gh project item-list <PROJECT_NUMBER> --owner "@me" --format json --jq ".items[] | select(.content.number==<ISSUE_NUMBER>) | .id")
echo $ITEM_ID
```

This will give you an ID that looks something like `PVTI_lA...`.

---

### Step 2: Find the Field and Option IDs

Next, you need to find the ID for the "Status" column itself, and the ID for the specific option within that column you want to move the card to.

Run this command to list all fields for your project:

```bash
GH_TOKEN=$GH_TOKEN_PROJECTS gh project field-list <PROJECT_NUMBER> --owner "@me" --format json
```

Look through the JSON output for the field with `"name": "Status"`. From that object, you will get two IDs:

1.  **Status Field ID**: The main `id` of the status field (e.g., `PVTSSF_lA...`).
2.  **Status Option ID**: The `id` of the specific option you want, found in the `options` array (e.g., `47fc9ee4` for "In Progress").

**Example JSON Snippet:**
```json
{
  "id": "PVTSSF_lAHOAI5ECc4BXL_9zhSaoe0",  // <-- This is the Status Field ID
  "name": "Status",
  "options": [
    {
      "id": "f75ad846",
      "name": "Todo"
    },
    {
      "id": "47fc9ee4", // <-- This is the Status Option ID for "In Progress"
      "name": "In Progress"
    },
    {
      "id": "98236657",
      "name": "Done"
    }
  ]
}
```

---

### Step 3: Move the Issue

Finally, use the `gh project item-edit` command with all the IDs you've collected. You also need the global Project ID for the `--project-id` flag. You can get this from `gh project list --format json`.

```bash
# Command to move the item
GH_TOKEN=$GH_TOKEN_PROJECTS gh project item-edit 
  --project-id "<PROJECT_ID>" 
  --id "<ITEM_ID>" 
  --field-id "<STATUS_FIELD_ID>" 
  --single-select-option-id "<STATUS_OPTION_ID>"
```

Replace the placeholders with the actual IDs. If successful, the command will print `Edited item "<Your Issue Title>"`.
