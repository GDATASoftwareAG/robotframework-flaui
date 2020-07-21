using System;
using System.Windows.Forms;

namespace NotifierTest
{
    public partial class Notifier : Form
    {
        public Notifier()
        {
            InitializeComponent();

            var aTimer = new Timer
            {
                Interval = 8000,
                Enabled = true,
            };

            aTimer.Tick += CloseWindow;
        }

        public void CloseWindow(object source, EventArgs e)
        {
            Close();
        }
    }
}
