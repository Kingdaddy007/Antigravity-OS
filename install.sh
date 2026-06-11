#!/usr/bin/env bash
# Anti-Gravity OS — Mac/Linux Installer
# Run: ./install.sh

# ─── Colors ──────────────────────────────────────────────────────────────────
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
DARKCYAN='\033[0;36m'
NC='\033[0m' # No Color

function step()    { echo -e "\n${CYAN}▶ $1${NC}"; }
function success() { echo -e "  ${GREEN}✓ $1${NC}"; }
function warn()    { echo -e "  ${YELLOW}⚠ $1${NC}"; }
function ask()     { echo -e "\n${WHITE}$1${NC}"; }
function header()  {
    echo -e "\n${DARKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "   ${CYAN}Anti-Gravity OS — Installer v1.2${NC}"
    echo -e "${DARKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

header

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOBAL_SOURCE="$SCRIPT_ROOT/global"

GLOBAL_CONFIG=""
IDE=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --global-config) GLOBAL_CONFIG="$2"; shift ;;
        --ide) IDE="$2"; shift ;;
        *) warn "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# ─── Step 1: Global config target ─────────────────────────────────────────────
if [ -z "$GLOBAL_CONFIG" ]; then
    if [ -z "$IDE" ]; then
        ask "Which IDE are you using?"
        echo ""
        echo "  [1] Google AI Studio / Gemini   → ~/.gemini/antigravity/"
        echo "  [2] Cursor                      → ~/.cursor/rules/"
        echo "  [3] Windsurf                    → ~/.codeium/windsurf/memories/"
        echo "  [4] VS Code (Copilot)           → .github/ in project root"
        echo "  [5] OpenCode                    → ~/.config/opencode/"
        echo "  [6] Custom path"
        echo ""
        read -p "Enter 1–6: " IDE_CHOICE
        IDE="$IDE_CHOICE"
    fi

    case "$IDE" in
        1) GLOBAL_CONFIG="$HOME/.gemini/antigravity" ;;
        2) GLOBAL_CONFIG="$HOME/.cursor/rules" ;;
        3) GLOBAL_CONFIG="$HOME/.codeium/windsurf/memories" ;;
        4) GLOBAL_CONFIG="$(pwd)/.github/antigravity" ;;
        5) GLOBAL_CONFIG="$HOME/.config/opencode" ;;
        6) 
            ask "Enter the full path to your global config folder:"
            read -p "> " GLOBAL_CONFIG
            # Expand tilde if present
            GLOBAL_CONFIG="${GLOBAL_CONFIG/#\~/$HOME}"
            ;;
        *) 
            warn "Unrecognised choice. Defaulting to ~/.gemini/antigravity/"
            GLOBAL_CONFIG="$HOME/.gemini/antigravity"
            ;;
    esac
fi

# ─── Step 2: Install Global Layer ────────────────────────────────────────────
step "Installing OS → $GLOBAL_CONFIG"

if [ ! -d "$GLOBAL_CONFIG" ]; then
    mkdir -p "$GLOBAL_CONFIG"
    success "Created configuration directory: $GLOBAL_CONFIG"
fi

step "Cleaning target directory..."
rm -rf "$GLOBAL_CONFIG"/*
success "Target ready."

cp -R "$GLOBAL_SOURCE/"* "$GLOBAL_CONFIG/"
success "Copied OS files successfully."

# ─── Step 2.5: User Personalisation check ─────────────────────────────────────
ask "Enter your name (leave blank for generic setup):"
read -p "> " USER_NAME

IS_BELOVED=false
if [[ "$USER_NAME" =~ [Bb]eloved ]] || [[ "$USER_NAME" =~ [Gg]odswill ]] || [[ "$USER_NAME" =~ [Gg]od\'s\ sweet ]] || [[ "$USER" =~ [Gg]odsw ]]; then
    IS_BELOVED=true
fi

if [ "$IS_BELOVED" = true ]; then
    step "Installing custom profile for Beloved..."
    TARGET_GEMINI="$GLOBAL_CONFIG/GEMINI.md"
    BELOVED_SOURCE="$GLOBAL_CONFIG/GEMINI-BELOVED.md"
    if [ -f "$BELOVED_SOURCE" ]; then
        cp "$BELOVED_SOURCE" "$TARGET_GEMINI"
        success "Loaded custom prompt constitution (Beloved configuration)."
    fi
fi

# Clean up GEMINI-BELOVED.md from target so it doesn't clutter or expose personal info
TARGET_BELOVED="$GLOBAL_CONFIG/GEMINI-BELOVED.md"
if [ -f "$TARGET_BELOVED" ]; then
    rm -f "$TARGET_BELOVED"
fi

# ─── Step 2.6: Interactive Profile Customisation ──────────────────────────────
if [ "$IS_BELOVED" = false ]; then
    ask "Would you like to customize your GEMINI.md master prompt now? [y/n]"
    read -p "> " CUSTOMIZE
    if [[ "$CUSTOMIZE" =~ ^[Yy]$ ]]; then
        step "Customizing your GEMINI.md profile..."
        
        read -p "Enter your Name/Nickname: " REAL_NAME
        [ -z "$REAL_NAME" ] && REAL_NAME="[Your Name]"
        
        read -p "Enter your Location (e.g. London-based): " LOCATION
        [ -z "$LOCATION" ] && LOCATION="[Your Location]"
        
        read -p "Describe your Work Style (e.g. sprint-based, steady-paced): " WORK_STYLE
        [ -z "$WORK_STYLE" ] && WORK_STYLE="steady-paced and task-focused."
        
        read -p "Describe your Execution Patterns (e.g. how you handle project milestones): " EXECUTION
        [ -z "$EXECUTION" ] && EXECUTION="finishes task milestones before shifting scope."
        
        read -p "Specify your rule for Decisions & Clarity (e.g. move at 70% clarity): " CLARITY
        [ -z "$CLARITY" ] && CLARITY="move forward once clarity is good enough (70% rule)."
        
        read -p "Specify your rule for Communication Patterns (e.g. direct, clear): " COMM_PATTERNS
        [ -z "$COMM_PATTERNS" ] && COMM_PATTERNS="direct, clear, and highlights blockers early."
        
        read -p "Detail your Resource Constraints (e.g. rate limits, budget): " RESOURCES
        [ -z "$RESOURCES" ] && RESOURCES="none specified."
        
        read -p "Describe your Quality Standard (e.g. clean code, test coverage): " QUALITY
        [ -z "$QUALITY" ] && QUALITY="expects clean code and solid verification traces."

        GEMINI_PATH="$GLOBAL_CONFIG/GEMINI.md"
        if [ -f "$GEMINI_PATH" ]; then
            if command -v perl >/dev/null 2>&1; then
                perl -pi -e "s/\[Your Name\]/$REAL_NAME/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Your Location\]/$LOCATION/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Describe your work pace, e\.g\., sprint-based, steady-paced, 1-3 day pushes, etc\.\]/$WORK_STYLE/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Detail how you start and finish projects, or rules for project milestones\.\]/$EXECUTION/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Specify your rule for taking action with incomplete information, e\.g\., decide at 70% clarity\.\]/$CLARITY/g" "$GEMINI_PATH"
                perl -pi -e "s/\[State how you communicate under stress, during wrap-ups, or standard routines\.\]/$COMM_PATTERNS/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Detail local resource realities, API\/financial budgets, or other environment limitations\.\]/$RESOURCES/g" "$GEMINI_PATH"
                perl -pi -e "s/\[Describe your expectations for visual quality, test coverage, code styles, or premium motion assets\.\]/$QUALITY/g" "$GEMINI_PATH"
            else
                sedi "s|\[Your Name\]|$REAL_NAME|g" "$GEMINI_PATH"
                sedi "s|\[Your Location\]|$LOCATION|g" "$GEMINI_PATH"
                sedi "s|\[Describe your work pace, e\.g\., sprint-based, steady-paced, 1-3 day pushes, etc\.\]|$WORK_STYLE|g" "$GEMINI_PATH"
                sedi "s|\[Detail how you start and finish projects, or rules for project milestones\.\]|$EXECUTION|g" "$GEMINI_PATH"
                sedi "s|\[Specify your rule for taking action with incomplete information, e\.g\., decide at 70% clarity\.\]|$CLARITY|g" "$GEMINI_PATH"
                sedi "s|\[State how you communicate under stress, during wrap-ups, or standard routines\.\]|$COMM_PATTERNS|g" "$GEMINI_PATH"
                sedi "s|\[Detail local resource realities, API/financial budgets, or other environment limitations\.\]|$RESOURCES|g" "$GEMINI_PATH"
                sedi "s|\[Describe your expectations for visual quality, test coverage, code styles, or premium motion assets\.\]|$QUALITY|g" "$GEMINI_PATH"
            fi
            success "Your personalized GEMINI.md has been generated!"
        fi
    fi
fi

# ─── Step 3: Dynamic Path URI Configuration ────────────────────────────────────
step "Configuring Absolute System Paths..."
TARGET_URI="file://$GLOBAL_CONFIG"
success "Target system URI resolved: $TARGET_URI"

replace_count=0
# Find all markdown files and substitute {{GLOBAL_CONFIG_URI}} with $TARGET_URI
# Usage of sed requires different syntax passing on mac vs linux
sedi() {
    case $(uname) in
        Darwin*) sed -i '' "$@" ;;
        *) sed -i "$@" ;;
    esac
}

while IFS= read -r -d '' file; do
    if grep -q "{{GLOBAL_CONFIG_URI}}" "$file"; then
        sedi "s|{{GLOBAL_CONFIG_URI}}|$TARGET_URI|g" "$file"
        replace_count=$((replace_count + 1))
    fi
done < <(find "$GLOBAL_CONFIG" -type f -name "*.md" -print0)

success "Re-wrote system URIs in $replace_count configuration files."

# ─── Step 4: Summary ─────────────────────────────────────────────────────────
echo -e "\n${DARKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "   ${GREEN}Anti-Gravity OS — Installation Complete${NC}"
echo -e "${DARKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "${WHITE}  GLOBAL SYSTEM installed at:"
echo -e "    $GLOBAL_CONFIG\n"
echo -e "  Next steps:"
echo -e "    1. Fill in your context files (contexts/stack-context.md, etc.)"
echo -e "    2. Tell your AI: \"Read GEMINI.md\" or configure it as your master prompt.\n${NC}"

echo -e "${DARKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
