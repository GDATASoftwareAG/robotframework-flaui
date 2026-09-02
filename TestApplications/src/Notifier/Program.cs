using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NotifierTest
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            if (args.Length == 1)
            {
                if (args[0] == "Delayed")
                {
                    Thread.Sleep(3000);
                }
                RunNotifierWithoutTimer(args);
            }
            if(args.Length >= 1)
            {
                RunNotifierWithoutTimer(args);
            }
            else
            {
                Application.Run(new Notifier());
            }
            
        }

        static void RunNotifierWithoutTimer(string[] args)
        {
            var title = args.Aggregate("", (current, arg) => current + arg);
            Application.Run(new Notifier(title, true));
        }
    }
}
