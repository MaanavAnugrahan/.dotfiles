require'colorizer'.setup()

return require('packer').startup(function()
    use 'wbthomason/packer.nvim'
    use 'lervag/vimtex'
    use 'nvim-telescope/telescope-symbols.nvim'
    use 'nvim-telescope/telescope-media-files.nvim'
    use 'renerocksai/calendar-vim'
    use 'preservim/vim-markdown'
    use 'godlygeek/tabular'
    use 'renerocksai/telekasten.nvim'
    use 'norcalli/nvim-colorizer.lua'
    use 'tribela/vim-transparent'
    use {'akinsho/bufferline.nvim', requires = 'kyazdani42/nvim-web-devicons'}
    use 'ishan9299/nvim-solarized-lua'
    use 'sainnhe/gruvbox-material'
    use 'kyazdani42/nvim-web-devicons'
    use 'shaunsingh/nord.nvim'
    use 'moll/vim-bbye'
    use({
	"catppuccin/nvim",
	as = "catppuccin"
})
    use 'kyazdani42/nvim-tree.lua'
    use {
        'nvim-lualine/lualine.nvim',
        requires = { 'kyazdani42/nvim-web-devicons', opt = true }
    }
    use 'neovim/nvim-lspconfig'
    use 'hrsh7th/nvim-cmp' -- Autocompletion plugin
    use 'hrsh7th/cmp-buffer' -- Autocompletion plugin
    use 'hrsh7th/cmp-path' -- Autocompletion plugin
    use 'hrsh7th/cmp-cmdline' -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin
    use 'onsails/lspkind-nvim'
    use 'nvim-lua/plenary.nvim'
    use {
    'goolord/alpha-nvim',
    config = function ()
        require'alpha'.setup(require'alpha.themes.dashboard'.config)
    end
}
    use {
    'williamboman/nvim-lsp-installer',
}
    use {
    'nvim-telescope/telescope.nvim',
    requires = { {'nvim-lua/plenary.nvim'} }
        }
    use 'lukas-reineke/indent-blankline.nvim'
    use {
        'nvim-treesitter/nvim-treesitter',
        run = ':TSUpdate'
    }
    use 'tpope/vim-commentary'
    use "EdenEast/nightfox.nvim"
    use 'nvim-lua/popup.nvim'
end)
