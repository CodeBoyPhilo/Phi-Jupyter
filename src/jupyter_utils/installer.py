#!/usr/bin/env python3

"""Install Jupyter configuration and utilities"""
import logging
import shutil
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


def run(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run command and handle errors"""
    logger.debug(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        logger.error(f"Command failed: {cmd}")
        if result.stderr:
            logger.error(f"Error output: {result.stderr}")
        sys.exit(1)
    return result


def ensure_dir(path: Path) -> None:
    """Ensure directory exists"""
    path.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {path}")


def link_or_copy(source: Path, target: Path) -> bool:
    """Create symlink or copy if symlink not supported"""
    if target.exists() or target.is_symlink():
        target.unlink()
    
    try:
        target.symlink_to(source)
        return True
    except (OSError, NotImplementedError):
        shutil.copy2(source, target)
        return False


def get_config_dir() -> Path:
    """Get the configuration directory"""
    # For editable install, config files are in source directory
    package_dir = Path(__file__).parent.parent.parent
    if (package_dir / "jupyterlab").exists():
        logger.debug(f"Found config in editable install: {package_dir}")
        return package_dir
    
    # For non-editable install, config files are bundled with package
    package_dir = Path(__file__).parent
    if (package_dir / "jupyterlab").exists():
        logger.debug(f"Found config in package: {package_dir}")
        return package_dir
    
    logger.error("Configuration files not found!")
    logger.error("This package may not have been installed correctly.")
    sys.exit(1)


def install_jupyterlab_settings(config_dir: Path, home: Path) -> None:
    """Install JupyterLab settings"""
    logger.info("1️⃣  Installing JupyterLab settings...")
    logger.info("─" * 60)
    
    jupyter_settings_dir = home / ".jupyter" / "lab" / "user-settings"
    ensure_dir(jupyter_settings_dir)
    
    source_settings = config_dir / "jupyterlab" / "settings"
    if not source_settings.exists():
        logger.warning(f"Settings directory not found: {source_settings}")
        return
    
    linked_count = 0
    copied_count = 0
    
    for item in source_settings.rglob("*"):
        if item.is_file():
            rel_path = item.relative_to(source_settings)
            target = jupyter_settings_dir / rel_path
            ensure_dir(target.parent)
            
            if link_or_copy(item, target):
                logger.info(f"  ✓ Linked {rel_path}")
                linked_count += 1
            else:
                logger.info(f"  ✓ Copied {rel_path}")
                copied_count += 1
    
    if linked_count == 0 and copied_count == 0:
        logger.warning("  No settings files found")
    else:
        logger.info(f"  📊 Total: {linked_count} linked, {copied_count} copied")


def install_ipython_startup(config_dir: Path, home: Path) -> None:
    """Install IPython startup scripts"""
    logger.info("\n2️⃣  Installing IPython startup scripts...")
    logger.info("─" * 60)
    
    ipython_startup = home / ".ipython" / "profile_default" / "startup"
    ensure_dir(ipython_startup)
    
    source_startup = config_dir / "ipython" / "startup"
    if not source_startup.exists():
        logger.warning(f"Startup directory not found: {source_startup}")
        return
    
    linked_count = 0
    copied_count = 0
    
    for script in source_startup.glob("*.py"):
        target = ipython_startup / script.name
        
        if link_or_copy(script, target):
            logger.info(f"  ✓ Linked {script.name}")
            linked_count += 1
        else:
            logger.info(f"  ✓ Copied {script.name}")
            copied_count += 1
    
    if linked_count == 0 and copied_count == 0:
        logger.warning("  No startup scripts found")
    else:
        logger.info(f"  📊 Total: {linked_count} linked, {copied_count} copied")


def main():
    """Main installation function"""
    config_dir = get_config_dir()
    home = Path.home()
    
    logger.info("=" * 60)
    logger.info("📦 Installing Jupyter Configuration")
    logger.info("=" * 60)
    logger.info(f"📁 Config directory: {config_dir}")
    logger.info(f"🏠 Home directory: {home}")
    logger.info("")
    
    try:
        # Install JupyterLab settings
        install_jupyterlab_settings(config_dir, home)
        
        # Install IPython startup scripts
        install_ipython_startup(config_dir, home)
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("✅ Installation complete!")
        logger.info("=" * 60)
        logger.info("")
        logger.info("Next steps:")
        logger.info("  • Restart JupyterLab to apply settings")
        logger.info("  • Test utilities: from jupyter_utils import ppprint")
        logger.info("")
        
    except Exception as e:
        logger.error("")
        logger.error("=" * 60)
        logger.error("❌ Installation failed!")
        logger.error("=" * 60)
        logger.error(f"Error: {e}")
        logger.exception("Full traceback:")
        sys.exit(1)


if __name__ == "__main__":
    main()
