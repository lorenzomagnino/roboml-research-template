"""Main entry point for the research template."""

import hydra
import wandb
from omegaconf import OmegaConf

from config.config_schema import Config


@hydra.main(version_base=None, config_path="config", config_name="defaults")
def main(cfg: Config) -> None:
    """Main function with Hydra configuration."""
    # Convert OmegaConf to structured config (optional, for type safety)
    # config = OmegaConf.structured(Config(**OmegaConf.to_container(cfg, resolve=True)))

    wandb.init(
        project=cfg.wandb.project,
        entity=cfg.wandb.entity,
        mode=cfg.wandb.mode,
        tags=cfg.wandb.tags,
        config=OmegaConf.to_container(cfg, resolve=True),
        name=cfg.experiment_name,
    )
    print("Configuration:")
    print(OmegaConf.to_yaml(cfg))

    # TODO: Add your training/inference logic here
    print("Main function executed successfully!")


if __name__ == "__main__":
    main()
