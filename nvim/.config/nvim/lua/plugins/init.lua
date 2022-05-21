return require('packer').startup(function()
use 'sainnhe/gruvbox-material'
use 'renerocksai/telekasten.nvim'
use 'tribela/vim-transparent'
-- Lua
use {
  "folke/which-key.nvim",
  config = function()
    require("which-key").setup {
    }
  end
}
-- use 'dracula/vim'
use 'lervag/vimtex'
use 'norcalli/nvim-colorizer.lua'
use 'renerocksai/calendar-vim'
use 'wbthomason/packer.nvim'
use {
  'nvim-lualine/lualine.nvim',
  requires = { 'kyazdani42/nvim-web-devicons', opt = true }
}
use {'akinsho/bufferline.nvim', tag = "*", requires = 'kyazdani42/nvim-web-devicons'}
-- use({
-- 	"catppuccin/nvim",
-- 	as = "catppuccin"
-- })
use 'nvim-lua/plenary.nvim'
use 'nvim-telescope/telescope.nvim'
use {
    'kyazdani42/nvim-tree.lua',
    requires = {
      'kyazdani42/nvim-web-devicons', -- optional, for file icon
    }
}
-- use 'shaunsingh/nord.nvim'
-- use "EdenEast/nightfox.nvim"
use "neovim/nvim-lspconfig"
use "williamboman/nvim-lsp-installer"
  -- cmp plugins
  use "hrsh7th/nvim-cmp" -- The completion plugin
  use "hrsh7th/cmp-buffer" -- buffer completions
  use "hrsh7th/cmp-path" -- path completions
  use "hrsh7th/cmp-cmdline" -- cmdline completions
  use "saadparwaiz1/cmp_luasnip" -- snippet completions
  use "hrsh7th/cmp-nvim-lsp"
  use "hrsh7th/cmp-nvim-lua"

  -- snippets
  use "L3MON4D3/LuaSnip" --snippet engine
  use "rafamadriz/friendly-snippets" -- a bunch of snippets to use
  use 'preservim/vim-markdown'
  use {
    'goolord/alpha-nvim',
    config = function ()
        require'alpha'.setup(require'alpha.themes.dashboard'.config)
    end
}
use 'tpope/vim-commentary'
end)
